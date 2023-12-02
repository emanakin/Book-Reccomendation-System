import { JwtPayload } from "jwt-decode";

export interface User {
  id: number,
  username?: string,
  password?: string
  location: string,
  age: number,
  user_details?: object
  token?: JwtPayload; 
}