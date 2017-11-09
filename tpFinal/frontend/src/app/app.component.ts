import { Component } from '@angular/core';
import { FileDropModule, UploadFile, UploadEvent } from 'ngx-file-drop/lib/ngx-drop';
import {AppService} from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [AppService]
})
export class AppComponent {
  title = 'app';
  constructor(public servicio: AppService) {}

  public files: UploadFile[] = [];
   public dropped(event: UploadEvent) {
     this.files = event.files;
     for (let file of event.files) {
       file.fileEntry.file(info => {
         console.log(info);
       });
     }
   }
   public fileOver(event) {
     console.log(event);
   }
   public fileLeave(event) {
     console.log(event);
   }
   public enviarArchivos() {
     console.log('enviando imagenes');
     this.servicio.enviarImagenes('algotengo que escribir aca', this.files).subscribe(res => {
       console.log('Implementar recepcion de predict cone stadistica');
     });
    }
   }