import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';

import { Users } from '../data/users';

@Injectable({
  providedIn: 'root'
})
export class CallExpressApiService {

  constructor(private http: HttpClient) { }

  public getUsers(): Observable<Users> {
    return this.http.get<Users>("api/users");
  }
}
