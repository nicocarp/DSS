import { Respuesta } from './respuesta';
import { RequestOptions, Http } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { Component } from '@angular/core';
import { FileDropModule, UploadFile, UploadEvent } from 'ngx-file-drop/lib/ngx-drop';
import { AppService } from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [AppService]
})
export class AppComponent {
  title = 'app';
  public error: String = '';
  public respuesta: Respuesta;

  constructor(public servicio: AppService, private http: Http) { }

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
    this.error = '';
    if (this.files[0].fileEntry) {
      this.servicio.enviarImagenes('/prediccion', this.files).subscribe(res => {
        this.respuesta = res.json();

      }, error => console.log(error),
        () => {
          if (this.respuesta.estado < 0) {
            this.error = this.respuesta.result;
          }
        });
    } else {
      alert('Hubo problemas al cargar la imágen');
    }
  }
  /*
    fileChange(event) {
      let fileList: FileList = event.target.files;
      if (fileList.length > 0) {
        let file: File = fileList[0];
        let formData: FormData = new FormData();
        formData.append('inputImagen', file, file.name);
  
  
        this.http.post('/prediccion', formData)
          .subscribe(
          data => console.log('success'),
          error => console.log(error)
          );
      }
    }*/
}
