// middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';
import { LocalStorageService, LocalStorageServiceItems } from './services/storage_services';

export function middleware(req: NextRequest) {
  // const token = req.cookies.get('access'); // Adjust based on your token storage method
  const token = LocalStorageService.instance.get(LocalStorageServiceItems.ACCESS_TOKEN); // Adjust based on your token storage method

  if (!token) {
    // Redirect to login page if no token is found
    return NextResponse.redirect(new URL('/login', req.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/','/home'], // Protect the /home route
};