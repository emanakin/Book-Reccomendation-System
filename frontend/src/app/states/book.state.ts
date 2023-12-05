import { State, Action, StateContext, Selector } from '@ngxs/store';
import { BookService } from '../services/book.service';
import {
    FetchSampleBooks,
    SendBaseRatingSample,
    FetchUserRatedBooks,
    FetchBooksBasedOnSimilarUsers,
    FetchBooksBasedOnPreferences,
    FetchPopularBooks
  } from '../actions/book.action';
import { Book, BookStateModel } from '../dto/book.model';
import { tap } from 'rxjs/operators';
import { Injectable } from '@angular/core';

@State<BookStateModel>({
    name: 'books',
    defaults: {
      sampleBooks: [],
      userRatedBooks: [],
      similarUserBooks: [],
      recommendedBooks: [],
      popularBooks: []
    }
  })
  @Injectable()
  export class BookState {
    constructor(private bookService: BookService) {}
  
    @Selector()
    static sampleBooks(state: BookStateModel): Book[] {
      return state.sampleBooks;
    }
    
    @Selector()
    static userRatedBooks(state: BookStateModel): Book[] {
      return state.userRatedBooks;
    }
    
    @Selector()
    static similarUserBooks(state: BookStateModel): Book[] {
      return state.similarUserBooks;
    }
    
    @Selector()
    static recommendedBooks(state: BookStateModel): Book[] {
      return state.recommendedBooks;
    }
    
    @Selector()
    static popularBooks(state: BookStateModel): Book[] {
      return state.popularBooks;
    }
    
    @Action(FetchSampleBooks)
    fetchSampleBooks({ patchState }: StateContext<BookStateModel>) {
      return this.bookService.getSampleBooks().pipe(
        tap((books) => {
          patchState({ sampleBooks: books });
        })
      );
    }
  
    @Action(SendBaseRatingSample)
    sendBaseRatingSample({ getState, patchState }: StateContext<BookStateModel>, { ratings }: SendBaseRatingSample) {
      return this.bookService.sendBaseRatingSample(ratings).pipe(
        tap((response) => {
          patchState({
            userRatedBooks: response.userRatedBooks
          });
        })
      );
    }
  
    @Action(FetchUserRatedBooks)
    fetchUserRatedBooks({ patchState }: StateContext<BookStateModel>) {
      return this.bookService.getUserRatedBooks().pipe(
        tap((books) => {
          patchState({ userRatedBooks: books });
        })
      );
    }
  
    @Action(FetchBooksBasedOnSimilarUsers)
    fetchBooksBasedOnSimilarUsers({ patchState }: StateContext<BookStateModel>) {
      return this.bookService.getBooksBasedOnSimilarUsers().pipe(
        tap((books) => {
          patchState({ similarUserBooks: books });
        })
      );
    }
  
    @Action(FetchBooksBasedOnPreferences)
    fetchBooksBasedOnPreferences({ patchState }: StateContext<BookStateModel>) {
      return this.bookService.getBooksBasedOnPreferences().pipe(
        tap((books) => {
          patchState({ recommendedBooks: books });
        })
      );
    }
  
    @Action(FetchPopularBooks)
    fetchPopularBooks({ patchState }: StateContext<BookStateModel>) {
      return this.bookService.getPopularBooks().pipe(
        tap((books) => {
          patchState({ popularBooks: books });
        })
      );
    }
  }
