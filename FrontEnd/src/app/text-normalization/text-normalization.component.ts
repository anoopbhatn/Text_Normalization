import { Component, OnInit } from '@angular/core';
import { TextNormalizationService } from './text-normalization.service';
import { ip } from '../ip';

@Component({
  selector: 'app-text-normalization',
  templateUrl: './text-normalization.component.html',
  styleUrls: ['./text-normalization.component.css']
})
export class TextNormalizationComponent implements OnInit {

  ip:string;
  action:string;
  private ipimport:ip

  constructor() {
    this.ipimport = new ip();
    this.ip = this.ipimport.ip;
    this.action = "http://" + this.ip + ":5000/post";
   }

  ngOnInit() {
  }

}
