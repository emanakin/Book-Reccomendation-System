import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LandingPageComponent } from './pages/landing-page/landing-page.component';
import { SignupPageComponent } from './pages/signup-page/signup-page.component';
import { LoginPageComponent } from './pages/login-page/login-page.component';
import { HttpClientModule } from '@angular/common/http';
import { AuthorDropdownComponent } from './pages/builder-page/author-dropdown/author-dropdown.component';
import { PublisherDropdownComponent } from './pages/builder-page/publisher-dropdown/publisher-dropdown.component';
import { MovieRateCarouselComponent } from './pages/builder-page/movie-rate-carousel/movie-rate-carousel.component';
import { NavigationBarComponent } from './shared/navigation-bar/navigation-bar.component';
import { BuilderPageComponent } from './pages/builder-page/builder-page.component';
import { ProgressBarComponent } from './pages/builder-page/progress-bar/progress-bar.component';
import { NgxsModule } from '@ngxs/store';
import { AuthState } from './states/auth.state';
import { AuthorState } from './states/author.state';
import { BookState } from './states/book.state';
import { PublisherState } from './states/publisher.state';
import { ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    LandingPageComponent,
    SignupPageComponent,
    LoginPageComponent,
    BuilderPageComponent,
    AuthorDropdownComponent,
    PublisherDropdownComponent,
    MovieRateCarouselComponent,
    NavigationBarComponent,
    ProgressBarComponent
  ],
  imports: [
    NgxsModule.forRoot([
      AuthorState,
      AuthState,
      BookState,
      PublisherState
    ]),
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
