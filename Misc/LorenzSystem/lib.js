function _1(md){return(
md`# The Lorenz System and its Initial Conditions
An interactive visualization of the Lorenz System aimed at building intuition.

*Hint: Start by just playing with the x, y, and z sliders*`
)}

function _2($0,htl){return(
htl.html`<div style='margin-left: 45%'>${$0}</div>`
)}

function _3(x1,y1,z1,sigma1,b1,r1,x2,y2,z2,sigma2,b2,r2,lorenz_animation,htl){return(
htl.html`<html>
 <head>
 </head>
 <body>
    <div class="container" style="display: flex; height: 30px;">
      <div style="width: 50%;text-align: center">
        <h2>Simulation 1:</h2>
      </div>
      <div style="width: 50%;text-align: center">
        <h2>Simulation 2:</h2>
      </div>
    </div>
    <div class="container" style="display: flex; height: 200px;">
      <div style="width: 5%"></div>
      <div style="width: 5%">
        (x)<br>
        (y)<br>
        (z)<br>
        (σ)<br>
        (b)<br>
        (r)<br>
        </div>  
      <div style="width: 30%">
        ${x1}
        ${y1}
        ${z1}
        ${sigma1}
        ${b1}
        ${r1}
        </div>
      <div style="width: 20%"></div>
      <div style="width: 5%">
        (x)<br>
        (y)<br>
        (z)<br>
        (σ)<br>
        (b)<br>
        (r)<br>
        </div>  
      <div style="width: 30%">
        ${x2}
        ${y2}
        ${z2}
        ${sigma2}
        ${b2}
        ${r2}
      </div>
    </div>
    <div class="container" style="display: flex; width: 100%; height: 100%">
      <div class="container" style="display: flex; width: 600px; height: 600px">
        ${lorenz_animation}
      </div>
    </div>
 </body>
</html>`
)}

function _second_view(run,run_simulation,x1,y1,z1,Plot,width)
{
  run
  const data = run_simulation(x1.value * 10,y1.value * 10,z1.value * 10,10,2.6667,28)
  const color_data = [{'dim': 'x', 'value': x1.value},
                      {'dim': 'y', 'value': y1.value},
                      {'dim': 'z', 'value': z1.value}]
  var second_plot = Plot.plot({
    grid: true,
    title: "Movement Isolated By Axis (Simulation 1)",
    width: width,
    style: {
      backgroundColor: '#293845',
      color: '#ffffff',
    },
    x: {label: "time", ticks: "none"},
    y: {label: "coordinate value"},
    color: {
      type: "categorical",
      domain: ['x','y','z'],
      range: ['#B54D4A','#71B656','#4AB2B5'],
      legend: true},
    marks: [
    Plot.frame(),

    Plot.dot(color_data, {
      x: 0,
      y: 'value',
      stroke: 'dim'
    }),
    Plot.line(data, {
      x: (d,i) => i,
      y: (d) => d["x"] / 10,
      stroke: '#B54D4A',
    }),
    Plot.line(data, {
      x: (d,i) => i,
      y: (d) => d["y"] / 10,
      stroke: '#71B656',
    }),
    Plot.line(data, {
      x: (d,i) => i,
      y: (d) => d["z"] / 10,
      stroke: '#4AB2B5',
    }),
    ]})
  return second_plot
}


function _5(md){return(
md`### About the Lorenz System
The [Lorenz System](https://en.wikipedia.org/wiki/Lorenz_system) is a system of ODEs that is defined as follows:

x' = σ(y - x)

y' = x(r - z) - y

z' = xy - bz

This system is very sensitive to initial conditions, but with some specific choices of σ, b, and r, one can observe some very interesting stable scenarios. For example σ = 10, b = 8/3, and r = 28 produces the characteristic Lorenz attractors irrespective of the initial spacial conditions. There is no analytical solution for the Lorenz system, so we use numerical methods to simulate the system with different initial conditions.

### About the Project:
Much of this project was aided by Gould's *An Introduction to Computer Simulation Methods*. The goal of this project was to help the viewer develop some intuition about the Lorenz System, as the high-dimensional nature of the system makes it hard to wrap your head around it when you are first introduced to it. A strong focus in this project was making the data visualization clear and accessible. The choice of color scheme was made to be color-blind friendly and visually appealing.

The data is simulated using the user-selected values for initial conditions, the Lorenz Equations, and a JavaScript ODE integrator using the [fourth-order Runge-Kutta](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods) method. I used NumJS to make the integrator in JavaScript, which is the \`run_simulation\` function in this notebook. I utilized a JavaScript library called THREE, as well as D3, to create the 3D display. The static view was done using Observable Plot and D3.

The most significant liberty I took in this project was mirroring the two simulations about the z axis in the animated view. This allows one to view two simulations with two separate initial conditions side-by-side, as in the stable state set by default, the Lorenz Attractors appear entirely in the positive z domain. In effect, the horizontal axes can be thought of as: \\[+x, +z, -x, +z]. `
)}

function _run(Inputs,html){return(
Inputs.button(html`<h1>GO!</h1>`)
)}

function* _lorenz_animation(run,THREE,x1,y1,z1,x2,y2,z2,run_simulation,sigma1,b1,r1,sigma2,b2,r2,d3,invalidation)
{  
    run
    let camera,
        renderer,
        scene,
        controls,
        cubeMesh,
        cubeGroup,
        folder,
        renderOnDemand=true,
        renderRequested=false,
        mainLight,
        material,
        height=400;
  
    init();
    function createCamera() {
        // Create a Camera
        const fov = 15; // AKA Field of View  
        const aspect = 1;
        const near = 0.1; // the near clipping plane
        const far = 1000; // the far clipping plane

        camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
        camera.position.set(-24, 20, -26);

    } 
    function createLights() {
        // Create a directional light
        const ambientLight = new THREE.HemisphereLight(0xddeeff, 0x202020, 8);
        scene.add(ambientLight);
    }
  
    function createMeshes() {
        
        const group = new THREE.Group();
       
        cubeGroup = group;

        // const curve = new THREE.CatmullRomCurve3([
        //   new THREE.Vector3(0, 0, 0),
        //   new THREE.Vector3(1, 0, 1),
        //   new THREE.Vector3(2, 1, 0),
        // ]);
        // const geometry = new THREE.TubeGeometry(curve, 64, 0.05, 8, false);
        // const material = new THREE.MeshStandardMaterial({ color: 0x00ff00, transparent: true, opacity: 0.9 });
        // const tube = new THREE.Mesh(geometry, material);
        // group.add(tube);
      
        const gridHelper2 = new THREE.GridHelper( 10, 10 , 'black', 'grey');
        gridHelper2.rotation.x = Math.PI * -.5;
        gridHelper2.material.transparent = true;
        gridHelper2.material.opacity = 0.3;
        gridHelper2.material.clipIntersection = true;
        group.add(gridHelper2);
        const gridHelper = new THREE.GridHelper( 10, 10 , 'black', 'grey');
        group.add(gridHelper);
      
        // Add the mesh to the scene
        scene.add(group);
    }

    function createAnimation(group){
        const dot_geo = new THREE.SphereGeometry( 0.05, 2, 16 )
          const dot_mat = new THREE.MeshStandardMaterial({
                color: 'grey',
                flatShading: true,
                opacity: 1,
                transparent: true, 
            })
        
          const point_1 = new THREE.Mesh(
            new THREE.SphereGeometry( 0.1, 32, 16 ),
            new THREE.MeshStandardMaterial({
                color: 'black',
            })
          );
          point_1.position.set(x1.value, y1.value,z1.value,)
          group.add(point_1)
          const point_2 = new THREE.Mesh(
            new THREE.SphereGeometry( 0.1, 32, 16 ),
            new THREE.MeshStandardMaterial({
                color: 'black',
            })
          );
          point_2.position.set(x2.value, y2.value,z2.value,)
          group.add(point_2)

        const data_1 = run_simulation(x1.value * 10,y1.value * 10,
                                        z1.value * 10,sigma1.value,b1.value,r1.value)
        const data_2 = run_simulation(x2.value * 10,y2.value * 10,
                                      z2.value * 10,sigma2.value,b2.value,r2.value)

        // const color_scheme_1 = d3.interpolateLab("#a598e3","#8a1313")
        // const color_scheme_2 = d3.interpolateLab("#ebd59b","#11829c")
      
        setTimeout(animate_simulation, 2000, data_1, point_1, d3.interpolateCividis)
        setTimeout(animate_simulation, 40000, data_2, point_2, d3.interpolateMagma, -1)
        
        function animate_simulation(data, point,color_scheme, reverse=1) {
          var mesh_path = Array(data.length)
          var dot_color = ""
          mesh_path[0] = new THREE.Mesh(dot_geo, dot_mat);
              mesh_path[0].position.set(
                data[0]['x'] / 10,
                data[0]['y'] / 10,
                data[0]['z'] / (10 * reverse))
          for (let i1 = 2; i1 < data.length; i1++){
            setTimeout(() => {
              dot_color = color_scheme(i1 / data.length)
              mesh_path[i1 - 1] = new THREE.Mesh(dot_geo,
                new THREE.MeshStandardMaterial({
                color: dot_color,
                flatShading: true,
            }));
              mesh_path[i1 - 1].position.set(
                data[i1]['x'] / 10,
                data[i1]['y'] / 10,
                data[i1]['z'] / (10 * reverse))
              group.add(mesh_path[i1 - 1])
              point.position.set(
                data[i1]['x'] / 10,
                data[i1]['y'] / 10,
                data[i1]['z'] / (10 * reverse))
              if (i1 == data.length - 1){
                console.log("returned")
                return true
              }
            }, i1 * 3)
          }
        }
    }
  
    function createRenderer() {
        // create the renderer
        renderer = new THREE.WebGLRenderer({
            antialias: true
        });

        renderer.setSize(600, 600);
        renderer.setPixelRatio(window.devicePixelRatio);
        renderer.gammaFactor = 2.2;
        renderer.gammaOutput = true;
        renderer.physicallyCorrectLights = true;
    }
  
    function init() {
          // create a Scene
          scene = new THREE.Scene();
  
          // Set the background color
          scene.background = new THREE.Color('#e8e6dc');
  
          createCamera();
          createLights();
          createMeshes();
          createAnimation(cubeGroup);
          createRenderer();
  
          controls = new THREE.OrbitControls(camera, renderer.domElement);
          invalidation.then(() => (controls.dispose(), renderer.dispose()));
     }
  
    function render() {
        renderer.render(scene, camera);
    }
  
    function update() {
       /*********** PUT ANIMATION LOGIC HERE **********/
       cubeGroup.rotation.y += 0.003;
       // cubeGroup.rotation.y += 0.01;
       //cubeGroup.rotation.z += 0.01;
       /***********************************************/
    }
  
    function onWindowResize() {
        camera.aspect = 1;
        camera.updateProjectionMatrix();
        renderer.setSize(600, 600)
    }
  
    window.addEventListener('resize', onWindowResize)

    function animationLoop(){
      update();
      render();
      // controls.update()
    }
    

    controls.update()
    controls.enabled = false;
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.rotateSpeed = 0.1;
    renderer.setAnimationLoop(animationLoop)
    
    invalidation.then(() => {
      controls.dispose();
      renderer.dispose();
      window.removeEventListener('resize', onWindowResize);
    });
    yield renderer.domElement
}


function _run_simulation(nj){return(
function run_simulation(x=0,y=0,z=0,sigma=10.0,b=2.6666,r=28) {
  let u_0 = nj.array([x,y,z])
  let t_0 = 0
  let t_end = 25
  var times = [t_0]
  var states = [to_coords(u_0)]
  var t = t_0
  let dt = 0.0025
  // let dt = 0.0018
  let dt_ = dt
  let data = []
  
  let u_1, k1, k2, k3, k4, dudt

  function to_coords(position_array){
    return {'x':position_array.get(0), 'y':position_array.get(1), 'z':position_array.get(2)}
  }
  
  function rhs(u) {
    dudt = nj.array([(-sigma * u.get(0)) + (sigma * u.get(1)),
                      (-u.get(0) * u.get(2)) + r * u.get(0) - u.get(1),
                      (u.get(0) * u.get(1)) - (b * u.get(2))])
    return dudt
  }
  function step(t, dt, u_0) {
      k1 = rhs(u_0)
      k2 = rhs(u_0.add(k1.multiply(dt / 2.0)))
      k3 = rhs(u_0.add(k2.multiply(dt / 2.0)))
      k4 = rhs(u_0.add(k3.multiply(dt)))
      u_1 = u_0.add((k1.add(k2.multiply(2)).add(k3.multiply(3)).add(k4)).multiply(dt / 6.0))
    return u_1
  }

  let iterations = t_end / dt
  for (let i1 = 0; i1 < iterations; i1++){
      dt_ = Math.min(dt,t_end-t)
      u_1 = step(t,dt_,u_0)
      t = t + dt_
      u_0 = u_1
      times.push(t)
      states.push(to_coords(u_1))
  }
      
  let t_vals = nj.array(times)
  return states 
}
)}

function _x1(Inputs){return(
Inputs.range([-10,10], {value: 0.1, step: 0.1})
)}

function _y1(Inputs){return(
Inputs.range([-10,10], {value: 0, step: 0.1})
)}

function _z1(Inputs){return(
Inputs.range([-10,10], {value: 0, step: 0.1})
)}

function _sigma1(Inputs){return(
Inputs.range([-20,20], {value: 10, step: 1})
)}

function _b1(Inputs){return(
Inputs.range([-10,10], {value: 2.66666, step: 0.1})
)}

function _r1(Inputs){return(
Inputs.range([-50,50], {value: 28, step: 1})
)}

function _x2(Inputs){return(
Inputs.range([-10,10], {vale: 0, step: 0.1})
)}

function _y2(Inputs){return(
Inputs.range([-10,10], {vale: 0, step: 0.1})
)}

function _z2(Inputs){return(
Inputs.range([-10,10], {vale: 0, step: 0.1})
)}

function _sigma2(Inputs){return(
Inputs.range([-20,20], {value: 10, step: 1})
)}

function _b2(Inputs){return(
Inputs.range([-10,10], {value: 2.66666, step: 0.1})
)}

function _r2(Inputs){return(
Inputs.range([-50,50], {value: 28, step: 1})
)}

async function _THREE(require)
{
  const THREE = window.THREE = await require("three@0.99.0/build/three.min.js");
  await require("three@0.99.0/examples/js/controls/OrbitControls.js").catch(() => {});
  return window.THREE;
}


function _d33d(require){return(
require('https://unpkg.com/d3-3d/build/d3-3d.min.js')
)}

function _nj(require){return(
require('https://cdn.jsdelivr.net/gh/nicolaspanel/numjs@0.15.1/dist/numjs.min.js')
)}

export default function define(runtime, observer) {
  const main = runtime.module();
  main.variable(observer()).define(["md"], _1);
  main.variable(observer()).define(["viewof run","htl"], _2);
  main.variable(observer()).define(["x1","y1","z1","sigma1","b1","r1","x2","y2","z2","sigma2","b2","r2","lorenz_animation","htl"], _3);
  main.variable(observer("second_view")).define("second_view", ["run","run_simulation","x1","y1","z1","Plot","width"], _second_view);
  main.variable(observer()).define(["md"], _5);
  main.variable(observer("viewof run")).define("viewof run", ["Inputs","html"], _run);
  main.variable(observer("run")).define("run", ["Generators", "viewof run"], (G, _) => G.input(_));
  main.variable(observer("lorenz_animation")).define("lorenz_animation", ["run","THREE","x1","y1","z1","x2","y2","z2","run_simulation","sigma1","b1","r1","sigma2","b2","r2","d3","invalidation"], _lorenz_animation);
  main.variable(observer("run_simulation")).define("run_simulation", ["nj"], _run_simulation);
  main.variable(observer("x1")).define("x1", ["Inputs"], _x1);
  main.variable(observer("y1")).define("y1", ["Inputs"], _y1);
  main.variable(observer("z1")).define("z1", ["Inputs"], _z1);
  main.variable(observer("sigma1")).define("sigma1", ["Inputs"], _sigma1);
  main.variable(observer("b1")).define("b1", ["Inputs"], _b1);
  main.variable(observer("r1")).define("r1", ["Inputs"], _r1);
  main.variable(observer("x2")).define("x2", ["Inputs"], _x2);
  main.variable(observer("y2")).define("y2", ["Inputs"], _y2);
  main.variable(observer("z2")).define("z2", ["Inputs"], _z2);
  main.variable(observer("sigma2")).define("sigma2", ["Inputs"], _sigma2);
  main.variable(observer("b2")).define("b2", ["Inputs"], _b2);
  main.variable(observer("r2")).define("r2", ["Inputs"], _r2);
  main.variable(observer("THREE")).define("THREE", ["require"], _THREE);
  main.variable(observer("d33d")).define("d33d", ["require"], _d33d);
  main.variable(observer("nj")).define("nj", ["require"], _nj);
  return main;
}
