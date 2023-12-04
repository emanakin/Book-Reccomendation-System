import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";

// book.service.ts
@Injectable({ providedIn: 'root' })
export class BookService {
  constructor(private http: HttpClient) {}

  getSampleBooks() {
    return this.http.get('/api/books/sample');
  }

  sendBaseRatingSample(ratings: Rating[]) {
    return this.http.post('/api/user/books/rating', ratings);
  }

  getUserRatedBooks() {
    return this.http.get('/api/user/books');
  }

  getBooksBasedOnSimilarUsers() {
    return this.http.get('/api/books/similar-users');
  }

  getBooksBasedOnPreferences() {
    return this.http.get('/api/books/recommendations');
  }

  getPopularBooks() {
    return this.http.get('/api/books/popular');
  }
}
