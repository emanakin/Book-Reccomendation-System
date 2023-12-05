import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Book, Rating } from "../dto/book.model";
import { Observable } from "rxjs";

@Injectable({ providedIn: 'root' })
export class BookService {
  constructor(private http: HttpClient) {}

  getSampleBooks(): Observable<Book[]> {
    return this.http.get<Book[]>('/api/books/sample');
  }

  sendBaseRatingSample(ratings: Rating[]): Observable<any> {
    return this.http.post('/api/user/books/rating', { ratings });
  }

  getUserRatedBooks(): Observable<Book[]> {
    return this.http.get<Book[]>('/api/user/books');
  }

  getBooksBasedOnSimilarUsers(): Observable<Book[]> {
    return this.http.get<Book[]>('/api/books/similar-users');
  }

  getBooksBasedOnPreferences(): Observable<Book[]> {
    return this.http.get<Book[]>('/api/books/recommendations');
  }

  getPopularBooks(): Observable<Book[]> {
    return this.http.get<Book[]>('/api/books/popular');
  }
}
