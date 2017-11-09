import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FileDropModule } from 'ngx-file-drop/lib/ngx-drop';
import { HttpModule } from '@angular/http';
import { AppComponent } from './app.component';
import { AppService } from './app.service';


@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    FileDropModule,
    HttpModule
  ],
  providers: [AppService],
  bootstrap: [AppComponent]
})
export class AppModule { }
