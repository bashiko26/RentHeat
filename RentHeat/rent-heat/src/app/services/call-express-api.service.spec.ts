import { TestBed, inject } from '@angular/core/testing';

import { CallExpressApiService } from './call-express-api.service';

describe('CallExpressApiService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [CallExpressApiService]
    });
  });

  it('should be created', inject([CallExpressApiService], (service: CallExpressApiService) => {
    expect(service).toBeTruthy();
  }));
});
