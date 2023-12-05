export interface Author {
    id: string;
    name: string;
}

  export interface AuthorStateModel {
    authors: Author[];
    preferredAuthors: Author[];
}