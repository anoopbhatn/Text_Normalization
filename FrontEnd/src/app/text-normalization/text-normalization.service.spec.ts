import { TestBed, inject } from '@angular/core/testing';

import { TextNormalizationService } from './text-normalization.service';

describe('TextNormalizationService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TextNormalizationService]
    });
  });

  it('should be created', inject([TextNormalizationService], (service: TextNormalizationService) => {
    expect(service).toBeTruthy();
  }));
});
