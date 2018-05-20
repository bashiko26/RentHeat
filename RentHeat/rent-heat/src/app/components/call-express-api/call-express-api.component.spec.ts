import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CallExpressApiComponent } from './call-express-api.component';

describe('CallExpressApiComponent', () => {
  let component: CallExpressApiComponent;
  let fixture: ComponentFixture<CallExpressApiComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CallExpressApiComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CallExpressApiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
