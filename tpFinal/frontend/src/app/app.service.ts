import { Injectable } from '@angular/core';
import { Http, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import { FileDropModule, UploadFile, UploadEvent } from 'ngx-file-drop/lib/ngx-drop';


@Injectable()
export class AppService {

    constructor(private http: Http) { }

    /**
     * Envia las imagenes y devuelve los resultados
     * @param url
     * @param files
     */
    enviarImagenes(url: string, files: UploadFile[]): Observable<any> {

        const formData: FormData = new FormData();

        let file: File;
        files[0].fileEntry.file(archivo => file = archivo);
        formData.append('inputImagen', file, file.name);
        /*
        let headers = new Headers();
        /** No need to include Content-Type in Angular 4 */
        /*
        headers.append('Content-Type', 'multipart/form-data');
        headers.append('Accept', 'application/json');
        let options = new RequestOptions({ headers: headers });
        */
        return this.http.post(url, formData);
    }
}
