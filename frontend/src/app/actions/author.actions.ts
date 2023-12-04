import { Author } from "../dto/author.model";

export class FetchAuthors {
    static readonly type = '[Author] Fetch Authors';
  }
  
  export class SendPreferredAuthors {
    static readonly type = '[Author] Send Preferred Authors';
    constructor(public preferredAuthors: Author[]) {}
  }
  