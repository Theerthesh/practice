import { Component } from '@angular/core';
import { UserService } from './Services/user.service';
import { User } from './Models/user.model';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule,FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  providers:[UserService]
  
})
export class AppComponent {
  users: User[] = [];
  filteredUsers: User[] = [];
  isLoading = true;
  errorMsg = '';
  searchUser = '';

  constructor(private userService: UserService) {}

  ngOnInit(): void {
    this.userService.getUsers().subscribe({
      next: (data) => {
        this.users = data;
        this.filteredUsers = data;
        this.isLoading = false;
      },
      error: () => {
        this.errorMsg = 'Failed to load users';
        this.isLoading = false;
      }
    });
  }

  onSearch(): void {
    const query = this.searchUser.toLowerCase();
    this.filteredUsers = this.users.filter(user =>
      user.name.toLowerCase().includes(query)
    );
  }
}
