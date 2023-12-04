export class FetchPublishers {
    static readonly type = '[Publisher] Fetch Publishers';
}
  
  export class SendPreferredPublishers {
    static readonly type = '[Publisher] Send Preferred Publishers';
    constructor(public payload: string[]) {}
}