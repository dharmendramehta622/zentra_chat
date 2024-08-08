import { LocalStorageService, LocalStorageServiceItems } from './storage_services';
 
function errorLogger(variables: any, error: any) {
    var _errorString = ` 
    Base URL: ${error}
    variables:$variables
    Encoded Variables : ${JSON.stringify(variables)}
    Error:${error}
    Error Message : ${error.message}
    `;
    console.error(_errorString);
}
function successLogger(variables: any, response: any) {
    var _successString = `
    Base Url:${response.headers}
    Variables: ${variables}
    Encoded Variables: ${JSON.stringify(variables)}
    status: ${response.status}
    Data:${response.data}
    `;
    console.log(_successString);
}

class ApiResponse{
    status: boolean;
    msg: any;
    constructor(status: boolean, msg: any) {
        this.status = status;
        this.msg = msg;
    }
    toString() {
        return `Status: ${this.status},Msg:${this.msg}`;
    }
}

var base_url = 'http://localhost:8000/';

class ApiBaseModel {
  //Axios client declaration
  axios: any;
  static instance: any;

  constructor(axios: any) {
    this.axios = axios;
    axios.interceptors.request.use(
      async (config: any) => {
        const token = LocalStorageService.instance.get(
          LocalStorageServiceItems.ACCESS_TOKEN
        ); 
        if (token) {
          config.headers.Authorization = `Bearer ${token}`;
        }
 
        return config;
      },
      (error: any) => {
        return Promise.reject(error);
      }
    );
  }

  async get(url: string, variables: any) {
    try {
      const response = this.axios({
        method: 'get',
        url: `${base_url}${url}`,
        data: variables,
      });
      let res = await response;
      successLogger(variables, response);
      return new ApiResponse(true, res.data);
    } catch (error: any) {
      errorLogger(variables, error);
      return new ApiResponse(false, error);
    }
  }

  async post(url: string, variables: any) {
    try {
      const response = this.axios({
        method: 'post',
        url: `${base_url}${url}`,
        data: variables,
      });
      let res = await response;
      successLogger(variables, response);
      return new ApiResponse(true, res.data);
    } catch (error: any) {
      errorLogger(variables, error);
      return new ApiResponse(false, error);
    }
  }

  async put(url: string, variables: any) {
    try {
      const response = this.axios({
        method: 'put',
        url: `${base_url}${url}`,
        data: variables,
      });
      let res = await response;
      successLogger(variables, response);
      return new ApiResponse(true, res.data);
    } catch (error: any) {
      errorLogger(variables, error);
      return new ApiResponse(false, error);
    }
  }

  async patch(url: string, variables: any) {
    try {
      const response = this.axios({
        method: 'patch',
        url: `${base_url}${url}`,
        data: variables,
      });
      let res = await response;
      successLogger(variables, response);
      return new ApiResponse(true, res.data);
    } catch (error: any) {
      errorLogger(variables, error);
      return new ApiResponse(false, error);
    }
  }

  async delete(url: string, variables: any) {
    try {
      const response = this.axios({
        method: 'delete',
        url: `${base_url}${url}`,
        data: variables,
      });
      let res = await response;
      successLogger(variables, response);
      return new ApiResponse(true, res.data);
    } catch (error: any) {
      errorLogger(variables, error);
      return new ApiResponse(false, error);
    }
  }
}

export { ApiBaseModel }