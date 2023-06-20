import logo from './logo.svg';
import './App.css';
import Robot from './components/Robot';


function App(props) {

  return (
    <div className="tc">
      <h1 className="title">ROBOFRIENDS</h1>
      <div className="pa2">
        <input type="search" placeholder="search robots" className="pa3 ba b--green bg-lightest-blue" />
      </div>
      <Robot />
      {/* <div style="overflow: scroll; border: 5px solid black; height: 800px;">
        <div>
          <div class="tc grow bg-light-green br3 pa3 ma2 dib bw2 shadow-5">
            <img alt="robots" src="https://robohash.org/1?size=200x200" />
            <div>
              <h2>Leanne Graham</h2>
              <p>Sincere@april.biz</p>
            </div>
          </div>
          <div class="tc grow bg-light-green br3 pa3 ma2 dib bw2 shadow-5">
            <img alt="robots" src="https://robohash.org/2?size=200x200" />
            <div>
              <h2>Ervin Howell</h2>
              <p>Shanna@melissa.tv</p>
            </div>
          </div>
          <div class="tc grow bg-light-green br3 pa3 ma2 dib bw2 shadow-5">
            <img alt="robots" src="https://robohash.org/3?size=200x200" />
            <div>
              <h2>Clementine Bauch</h2>
              <p>Nathan@yesenia.net</p>
            </div>
          </div>
          <div class="tc grow bg-light-green br3 pa3 ma2 dib bw2 shadow-5">
            <img alt="robots" src="https://robohash.org/4?size=200x200" />
            <div>
              <h2>Patricia Lebsack</h2>
              <p>Julianne.OConner@kory.org</p>
            </div>
          </div>
          <div class="tc grow bg-light-green br3 pa3 ma2 dib bw2 shadow-5">
            <img alt="robots" src="https://robohash.org/5?size=200x200" />
            <div>
              <h2>Chelsey Dietrich</h2>
              <p>Lucio_Hettinger@annie.ca</p>
            </div>
          </div>
          <div class="tc grow bg-light-green br3 pa3 ma2 dib bw2 shadow-5">
            <img alt="robots" src="https://robohash.org/6?size=200x200" />
            <div>
              <h2>Mrs. Dennis Schulist</h2>
              <p>Karley_Dach@jasper.info</p>
            </div>
          </div>
          <div class="tc grow bg-light-green br3 pa3 ma2 dib bw2 shadow-5">
            <img alt="robots" src="https://robohash.org/7?size=200x200" />
            <div>
              <h2>Kurtis Weissnat</h2>
              <p>Telly.Hoeger@billy.biz</p>
            </div>
          </div>
          <div class="tc grow bg-light-green br3 pa3 ma2 dib bw2 shadow-5">
            <img alt="robots" src="https://robohash.org/8?size=200x200" />
            <div>
              <h2>Nicholas Runolfsdottir V</h2>
              <p>Sherwood@rosamond.me</p>
            </div>
          </div>
          <div class="tc grow bg-light-green br3 pa3 ma2 dib bw2 shadow-5">
            <img alt="robots" src="https://robohash.org/9?size=200x200" />
            <div>
              <h2>Glenna Reichert</h2>
              <p>Chaim_McDermott@dana.io</p>
            </div>
          </div>
          <div class="tc grow bg-light-green br3 pa3 ma2 dib bw2 shadow-5">
            <img alt="robots" src="https://robohash.org/10?size=200x200" />
            <div>
              <h2>Clementina DuBuque</h2>
              <p>Rey.Padberg@karina.biz</p>
            </div>
          </div>
        </div> 
      </div>*/}
    </div>
  );
}

export default App;
