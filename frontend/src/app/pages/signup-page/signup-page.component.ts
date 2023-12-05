import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Store } from '@ngxs/store';
import { Signup } from 'src/app/actions/auth.action';


@Component({
  selector: 'app-signup-page',
  templateUrl: './signup-page.component.html',
  styleUrls: ['./signup-page.component.css']
})
export class SignupPageComponent {
  signupForm = new FormGroup({
    username: new FormControl('', [Validators.required]),
    password: new FormControl('', [Validators.required, Validators.minLength(6)]),
    confirmPassword: new FormControl('', [Validators.required]),
    location: new FormControl('', [Validators.required]),
    age: new FormControl('', [Validators.required, Validators.min(18)])
  });

  constructor(private store: Store) {}

  submitSignup() {
    if (this.signupForm.invalid) {
      return; 
    } 

    const { confirmPassword, username, password, location, age } = this.signupForm.value;
    const numericAge = +age;

    if (password !== confirmPassword) {
      this.signupForm.get('confirmPassword').setErrors({ confirmPasswordMismatch: true });
      return;
    }

    const userDetails = { username, password, location, age: numericAge };

    this.store.dispatch(new Signup(userDetails));
  }

  
}

