import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { CallExpressApiComponent } from './components/call-express-api/call-express-api.component';

const routes: Routes = [
  {path: 'users', component: CallExpressApiComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
