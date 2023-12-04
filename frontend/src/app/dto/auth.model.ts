import { User } from "./user.model";

export interface AuthStateModel {
    token: AuthToken | null;
    user: User | null; 
}

export interface AuthResponse {
    token: AuthToken;
    user: User; 
}

export interface AuthToken {
    exp: number;
    iat: number;
    userId: string;
}