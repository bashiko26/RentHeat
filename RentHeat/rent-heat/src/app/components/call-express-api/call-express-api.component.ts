import { Component, OnInit } from '@angular/core';
import { CallExpressApiService } from '../../services/call-express-api.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-call-express-api',
  templateUrl: './call-express-api.component.html',
  styleUrls: ['./call-express-api.component.scss'],
  providers: [ CallExpressApiComponent ]
})
export class CallExpressApiComponent implements OnInit {

  users: any;

  constructor(private callExpressApiService: CallExpressApiService) { }

  ngOnInit() {
    this.callExpressApiService.getUsers().subscribe(u => {
      this.users = u.users;
    });
  }

}
