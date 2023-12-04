import { State, Action, StateContext, Selector } from '@ngxs/store';
import { tap } from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { AuthService } from '../services/auth.service';
import { AuthStateModel, AuthToken } from "../dto/auth.model";
import { Login, Logout, Signup } from "../actions/auth.action";
import { Token } from '@angular/compiler';
import { User } from '../dto/user.model';

@State<AuthStateModel>({
  name: 'auth',
  defaults: {
    token: null,
    user: null
  }
})
@Injectable()
export class AuthState {
  constructor(private authService: AuthService) {}

  @Selector()
  static token(state: AuthStateModel) {
    return state.token;
  }

  @Selector()
  static isAuthenticated(state: AuthStateModel): boolean {
    return !!state.token;
  }

  @Action(Login)
  login({ patchState }: StateContext<AuthStateModel>, { payload }: Login) {
    return this.authService.login(payload).pipe(
      tap((result: { user: User, token: AuthToken }) => {
        patchState({
          token: result.token,
          user: result.user
        });
      })
    );
  }

  @Action(Signup)
  signup({ patchState }: StateContext<AuthStateModel>, { payload }: Signup) {
    return this.authService.signup(payload).pipe(
      tap((result: { user: User, token: AuthToken }) => {
        patchState({
          token: result.token,
          user: result.user
        });
      })
    );
  }

  @Action(Logout)
  logout({ setState }: StateContext<AuthStateModel>) {
    setState({
      token: null,
      user: null
    });
  }
}
