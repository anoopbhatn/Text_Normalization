import { Component, OnInit } from '@angular/core';
import { ip } from '../ip';

@Component({
  selector: 'app-about-us',
  templateUrl: './about-us.component.html',
  styleUrls: ['./about-us.component.css']
})
export class AboutUsComponent implements OnInit {

  ip:string;
  anoopsrc:string;
  shashanksrc:string;
  ipimport:ip;

  constructor() { 
    this.ipimport = new ip();
    this.ip = this.ipimport.ip;
    this.anoopsrc = "http://"+ this.ip +":8080/anoop.jpg";
    this.shashanksrc = "http://"+ this.ip +":8080/shashank.jpg";
  }

  ngOnInit() {
  }

}
