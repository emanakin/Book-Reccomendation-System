import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({ providedIn: 'root' })
export class PublisherService {
  constructor(private http: HttpClient) {}

  getPublishers() {
    return this.http.get<string[]>('/api/books/publishers');
  }

  sendPreferredPublishers(preferredPublishers: string[]) {
    return this.http.post<string[]>('/api/user/publishers', { publishers: preferredPublishers });
  }
}
