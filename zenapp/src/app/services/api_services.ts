
import axios from 'axios';
import { ApiBaseModel } from './api_base_service';
 


class AxiosServices extends ApiBaseModel { 
  
    static instance = new ApiBaseModel(axios);
    axios = axios.create({
      timeout: 1000,
    });
    constructor() {
      super(axios);
      if (ApiBaseModel.instance) {
        return ApiBaseModel.instance;
      }
      ApiBaseModel.instance = this;
    }
  }

export { AxiosServices };