import { Injectable } from "@angular/core";
import { HttpClient } from '@angular/common/http'
import { catchError, tap, throwError } from "rxjs";
import { Router } from '@angular/router';
import { User } from "../dto/user.model";
import * as jwt_decode from 'jwt-decode';
import { AuthResponse, AuthToken } from "../dto/auth.model";

const apiEndpoint = "http://127.0.0.1:5000/";

@Injectable({ providedIn: 'root' })
export class AuthService {
    
    constructor(private http: HttpClient, private router: Router) {}

    signup(user: User) {
        return this.http.post<AuthResponse>(
            apiEndpoint+'signup', { user })
        .pipe(  
            catchError(errorRes => {
                let errorMessage = 'An unknown error occurred!';
                if (errorRes.error && errorRes.error.message) {
                    errorMessage = errorRes.error.message +': ' + errorRes.status;
                }
                console.log(errorMessage);
                return throwError(errorMessage);
            }) 
        );
    }

    login(user: {username: string, password: string}) {
        return this.http.post<AuthResponse>(
        apiEndpoint+'login',{ user })
        .pipe(
            catchError(errorRes => {
                let errorMessage = 'An unknown error occurred!';
                if (errorRes.error && errorRes.error.message) {
                    errorMessage = errorRes.error.message +': ' + errorRes.status;
                }
                console.log(errorMessage);
                return throwError(errorMessage);
            }) 
        );
    }

    getToken(): string {
        const storedToken = localStorage.getItem('token');
        if (!storedToken) {
            return null;  
        }
        return JSON.parse(storedToken);
    }

    removeToken(): void {
        localStorage.removeItem('token');
    }

    getUserId(): string {
        const token = this.getToken();
        if (!token) return null;
        const decodedToken: AuthToken = jwt_decode.jwtDecode(token);
        return decodedToken.userId;
    }

    getDecodedToken(): AuthToken {
        const token = this.getToken();
        if (!token) return null;
        const decodedToken: AuthToken = jwt_decode.jwtDecode(token);
        console.log('token fetched:', decodedToken)
        return decodedToken;
    }

}