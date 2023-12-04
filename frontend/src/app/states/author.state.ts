// author.state.ts
import { State, Action, StateContext, Selector } from '@ngxs/store';
import { AuthorService } from '../services/author.service';
import { tap } from 'rxjs/operators';
import { FetchAuthors, SendPreferredAuthors } from '../actions/author.actions';
import { Author } from '../dto/author.model';

export interface AuthorStateModel {
  authors: Author[];
  preferredAuthors: Author[];
}

@State<AuthorStateModel>({
  name: 'authors',
  defaults: {
    authors: [],
    preferredAuthors: []
  }
})
export class AuthorState {
  constructor(private authorService: AuthorService) {}

  @Selector()
  static authors(state: AuthorStateModel): Author[] {
    return state.authors;
  }

  @Selector()
  static preferredAuthors(state: AuthorStateModel): Author[] {
    return state.preferredAuthors;
  }

  @Action(FetchAuthors)
  fetchAuthors({ patchState }: StateContext<AuthorStateModel>) {
    return this.authorService.getAuthors().pipe(tap((authors) => {
      patchState({ authors });
    }));
  }

  @Action(SendPreferredAuthors)
  sendPreferredAuthors({ getState, patchState }: StateContext<AuthorStateModel>, { preferredAuthors }: SendPreferredAuthors) {
    return this.authorService.sendPreferredAuthors(preferredAuthors).pipe(tap(() => {
      const state = getState();
      patchState({
        preferredAuthors: [...state.preferredAuthors, ...preferredAuthors]
      });
    }));
  }
}
