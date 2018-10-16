import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Http, Headers } from '@angular/http';
import { ip } from '../ip';

@Component({
  selector: 'app-after-normalize',
  templateUrl: './after-normalize.component.html',
  styleUrls: ['./after-normalize.component.css']
})
export class AfterNormalizeComponent implements OnInit {

  data;
  ip;
  private ipimport:ip;
  getUrl:string;
  headers;

  constructor(private http: HttpClient) {
    this.ipimport = new ip();
    this.ip = this.ipimport.ip;
    this.getUrl = 'http://'+this.ip+':5000/get';
   }

  ngOnInit() {
    console.log('hello');
    this.something();
  
  }

  something(){
    // this.headers = new HttpHeaders; 
    // this.headers.append('Access-Control-Allow-Origin', '*');
    // this.headers.append('Access-Control-Allow-Methods', 'GET');
    // ,this.headers

    this.http.get(this.getUrl)
    .subscribe(
      data => {
        console.log(data); 
        this.data=data;
      });
    }
}