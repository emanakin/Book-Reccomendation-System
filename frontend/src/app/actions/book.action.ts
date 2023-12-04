export class FetchSampleBooks {
    static readonly type = '[Book] Fetch Sample Books';
  }
  
  export class SendBaseRatingSample {
    static readonly type = '[Book] Send Base Rating Sample';
    constructor(public ratings: number[]) {}
  }
  
  export class FetchUserRatedBooks {
    static readonly type = '[Book] Fetch User Rated Books';
  }
  
  export class FetchBooksBasedOnSimilarUsers {
    static readonly type = '[Book] Fetch Books Based on Similar Users';
  }
  
  export class FetchBooksBasedOnPreferences {
    static readonly type = '[Book] Fetch Books Based on Preferences';
  }
  
  export class FetchPopularBooks {
    static readonly type = '[Book] Fetch Popular Books';
  }
  