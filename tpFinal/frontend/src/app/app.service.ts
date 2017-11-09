import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
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
        return this.http.post(url, files)
        .do(res => console.log('enviando imagenes'))
        .map(res => res.json());
    }
}