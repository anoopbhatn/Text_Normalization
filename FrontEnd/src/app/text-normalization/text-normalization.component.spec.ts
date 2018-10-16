import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TextNormalizationComponent } from './text-normalization.component';

describe('TextNormalizationComponent', () => {
  let component: TextNormalizationComponent;
  let fixture: ComponentFixture<TextNormalizationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TextNormalizationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TextNormalizationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
