import { Respuesta } from './respuesta';
import { RequestOptions, Http } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { Component, Input } from '@angular/core';
import { FileDropModule, UploadFile, UploadEvent } from 'ngx-file-drop/lib/ngx-drop';
import { AppService } from './app.service';
import { element } from 'protractor';
import { NgForm, NgModel } from '@angular/forms';

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
  @Input() public url: any;

  constructor(public servicio: AppService, private http: Http) { }

  public files: UploadFile[] = [];
  public cargando: Boolean = false;
  public nombreImagen: String;


  public dropped(event: any) {


    this.files = event.files;
    for (let file of event.files) {
      file.fileEntry.file(info => {
        console.log(info);
        this.crearImagen(info);

      });
    }
    console.log('Fin....droped');
  }

  public crearImagen(data: Blob) {
    console.log('creandoimagen');
    let reader = new FileReader();
    reader.addEventListener('load', () => {
      this.url = reader.result;
      this.cargando = true;
      console.log(this.url);

    }, false);
    if (data) {
      console.log('reader');
      reader.readAsDataURL(data);
    }
  }


  public fileOver(event) {
  }
  public fileLeave(event) {

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

  fileChange(event) {
    let fileList: FileList = event.target.files;
    if (fileList.length > 0) {
      let file: File = fileList[0];
      let formData: FormData = new FormData();
      formData.append('inputImagen', file, file.name);


      this.http.post('/prediccion', formData)
        .subscribe(
        data => {
          console.log('success');
          this.respuesta = data.json();
        },
        error => console.log(error)
        );
    }

  }
}
