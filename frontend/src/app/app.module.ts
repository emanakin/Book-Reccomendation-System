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

@NgModule({
  declarations: [
    AppComponent,
    LandingPageComponent,
    SignupPageComponent,
    LoginPageComponent,
    AuthorDropdownComponent,
    PublisherDropdownComponent,
    MovieRateCarouselComponent,
    NavigationBarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
