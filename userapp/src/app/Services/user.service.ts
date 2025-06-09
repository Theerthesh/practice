import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { User } from '../Models/user.model';
import { Api } from '../../assets/environement';

@Injectable({ providedIn: 'root' })
export class UserService {
  private readonly api = 'https://jsonplaceholder.typicode.com/users';

  constructor(private http: HttpClient,) {}

  getUsers(): Observable<User[]> {
    return this.http.get<User[]>(Api.user);
  }
}
