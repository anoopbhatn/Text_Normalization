import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { provideRoutes} from '@angular/router';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { AboutTextNormalizationComponent } from './about-text-normalization/about-text-normalization.component';
import { TextNormalizationComponent } from './text-normalization/text-normalization.component';
import { AboutUsComponent } from './about-us/about-us.component';
import { HttpClientModule, HttpClient, HttpHandler } from '@angular/common/http';
import { HttpModule } from '@angular/http';
import { TextNormalizationService } from './text-normalization/text-normalization.service';
import { AfterNormalizeComponent } from './after-normalize/after-normalize.component';

const routes: Routes = [
  { path: 'about', component: AboutTextNormalizationComponent },
  { path: 'textnormalize', component: TextNormalizationComponent },
  { path: 'details', component: AboutUsComponent },
  { path: 'afternormalize', component: AfterNormalizeComponent }
];

@NgModule({
  declarations: [
    AppComponent,
    AboutTextNormalizationComponent,
    TextNormalizationComponent,
    AboutUsComponent,
    AfterNormalizeComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    HttpModule,
    RouterModule.forRoot(
      routes),
  ],
  providers: [TextNormalizationService, HttpClientModule,HttpClient],
  bootstrap: [AppComponent]
})
export class AppModule { }
