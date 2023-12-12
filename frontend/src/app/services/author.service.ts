import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Author } from '../dto/author.model';

@Injectable({ providedIn: 'root' })
export class AuthorService {
  constructor(private http: HttpClient) {}

  getAuthors(): Observable<Author[]> {
    return this.http.get<Author[]>('/api/books/authors');
  }

  sendPreferredAuthors(preferredAuthors: Author[]): Observable<any> {
    return this.http.post('/api/user/authors', { authors: preferredAuthors });
  }
}

