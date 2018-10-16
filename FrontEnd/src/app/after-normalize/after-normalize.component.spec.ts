import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AfterNormalizeComponent } from './after-normalize.component';
import { HttpClientModule, HttpClient, HttpHandler } from '@angular/common/http';

describe('AfterNormalizeComponent', () => {
  let component: AfterNormalizeComponent;
  let fixture: ComponentFixture<AfterNormalizeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AfterNormalizeComponent ],
      providers:[HttpClientModule,HttpClient, HttpHandler]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AfterNormalizeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
