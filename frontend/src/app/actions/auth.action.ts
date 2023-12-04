import { User } from "../dto/user.model";

export class Login {
    static readonly type = '[Auth] Login';
    constructor(public payload: { username: string; password: string }) {}
}

export class Signup {
    static readonly type = '[Auth] Signup';
    constructor(public payload: User) {}
}

export class Logout {
    static readonly type = '[Auth] Logout';
}
  