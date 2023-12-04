import { State, Action, StateContext, Selector } from '@ngxs/store';
import { BookService } from '../services/book.service';
import {
  FetchSampleBooks,
  SendBaseRatingSample,
  FetchUserRatedBooks,
  FetchBooksBasedOnSimilarUsers,
  FetchBooksBasedOnPreferences,
  FetchPopularBooks
} from './book.actions';
import { tap } from 'rxjs/operators';

export interface BookStateModel {
  sampleBooks: Book[];
  userRatedBooks: Book[];
  similarUserBooks: Book[];
  recommendedBooks: Book[];
  popularBooks: Book[];
}

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
export class BookState {
  constructor(private bookService: BookService) {}

  @Selector()
  static getSampleBooks(state: BookStateModel) {
    return state.sampleBooks;
  }

  // ... Other selectors for different book lists

  @Action(FetchSampleBooks)
  fetchSampleBooks({ patchState }: StateContext<BookStateModel>) {
    return this.bookService.getSampleBooks().pipe(tap((sampleBooks) => {
      patchState({ sampleBooks });
    }));
  }

  @Action(SendBaseRatingSample)
  sendBaseRatingSample({ getState, patchState }: StateContext<BookStateModel>, { ratings }: SendBaseRatingSample) {
    return this.bookService.sendBaseRatingSample(ratings).pipe(tap((updatedRatings) => {
      const state = getState();
      patchState({ userRatedBooks: updatedRatings });
    }));
  }

  // ... Implement other actions similarly
}
