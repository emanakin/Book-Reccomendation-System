import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthService } from '../services/auth.service'; 
import * as jwt_decode from 'jwt-decode';
import { AuthToken } from '../dto/authToken.model'; 

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(
    private authService: AuthService,
    private router: Router
  ) {}

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): boolean | Observable<boolean> | Promise<boolean> {
    const token = this.authService.getToken();
    let decodedToken: AuthToken;

    if (!token) {
      this.router.navigate(['/login']);
      return false;
    }

    try {
      decodedToken = jwt_decode.jwtDecode(token);
    } catch (error) {
      console.error("Invalid token:", error);
      this.authService.removeToken();
      this.router.navigate(['/login']);
      return false;
    }

    const currentTime = new Date().getTime() / 1000;
    if (decodedToken.exp < currentTime) {
      console.log('Token expired.');
      this.authService.removeToken();
      this.router.navigate(['/login']);
      return false;
    }

    if (state.url === '/login' || state.url === '/signup') {
      this.router.navigate(['/home']);
      return false;
    }

    return true;
  }
}
