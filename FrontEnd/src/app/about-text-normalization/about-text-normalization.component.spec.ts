import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AboutTextNormalizationComponent } from './about-text-normalization.component';

describe('AboutTextNormalizationComponent', () => {
  let component: AboutTextNormalizationComponent;
  let fixture: ComponentFixture<AboutTextNormalizationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AboutTextNormalizationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AboutTextNormalizationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
