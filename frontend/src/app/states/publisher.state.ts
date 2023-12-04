import { Action, Selector, State, StateContext } from "@ngxs/store";
import { PublisherStateModel } from "../dto/publisher.model";
import { Injectable } from "@angular/core";
import { PublisherService } from "../services/publisher.service";
import { FetchPublishers, SendPreferredPublishers } from "../actions/publisher.actions";
import { tap } from "rxjs";

@State<PublisherStateModel>({
    name: 'publishers',
    defaults: {
      publishers: [],
      preferredPublishers: []
    }
  })
  @Injectable()
  export class PublisherState {
    constructor(private publisherService: PublisherService) {}
  
    @Selector()
    static getPublishersList(state: PublisherStateModel) {
      return state.publishers;
    }
  
    @Selector()
    static getPreferredPublishers(state: PublisherStateModel) {
      return state.preferredPublishers;
    }
  
    @Action(FetchPublishers)
    fetchPublishers({ patchState }: StateContext<PublisherStateModel>) {
      return this.publisherService.getPublishers().pipe(tap((publishers) => {
        patchState({ publishers });
      }));
    }
  
    @Action(SendPreferredPublishers)
    sendPreferredPublishers({ getState, patchState }: StateContext<PublisherStateModel>, { payload }: SendPreferredPublishers) {
      return this.publisherService.sendPreferredPublishers(payload).pipe(tap((preferredPublishers) => {
        const state = getState();
        patchState({
          preferredPublishers: [...state.preferredPublishers, ...preferredPublishers]
        });
      }));
    }
  }