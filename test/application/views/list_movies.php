<div class="main-panel">
      <!-- Navbar -->
      <nav class="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top " >
        <div class="container-fluid"style="background:#fff">
          <div class="navbar-wrapper" >
            <a class="navbar-brand" >Movie list</a>
          </div>
          <button class="navbar-toggler" type="button" data-toggle="collapse" aria-controls="navigation-index" aria-expanded="false" aria-label="Toggle navigation">
            <span class="sr-only">Toggle navigation</span>
            <span class="navbar-toggler-icon icon-bar"></span>
            <span class="navbar-toggler-icon icon-bar"></span>
            <span class="navbar-toggler-icon icon-bar"></span>
          </button>
          <div class="collapse navbar-collapse justify-content-end">
            
            <ul class="navbar-nav">
             
              <li class="nav-item dropdown">
                <a class="nav-link" href="#pablo" id="navbarDropdownProfile" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  <i class="material-icons">person</i>
                  <p class="d-lg-none d-md-block">
                    Account
                  </p>
                </a>
                <div class="dropdown-menu dropdown-menu-right" aria-labelledby="navbarDropdownProfile">
                  <a class="dropdown-item" href="#">Iniciar sesión</a>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </nav>

<div class="content">
        <div class="container-fluid">
          <div class="row">
            <div class="col-md-12">
              <div class="card">
                <div class="card-header card-header-primary">
                  <h4 class="card-title ">Movies</h4>
                  <p class="card-category"> registered movies</p>
                </div>
                <div class="card-body">
                  <div class="table-responsive">
                    <table class="table">
                      <thead class=" text-primary">
                      <th></th>
                        <th>Availability</th>
                        <th>Title</th>
                        <th>Stock</th>
                        <th>Sale</th>
                        <th>Rent</th>
                        
                      </thead>
                      <tbody>
                      <?php foreach ($movies as $item) { ?>
                        <tr>
                        <td class="td-actions text-right">
                                    <div>
                                        <div class="dropdown">
                                            <button href="#pablo" class="dropdown-toggle btn btn-warning btn-round btn-block" data-toggle="dropdown" aria-expanded="false">
                                                <i class="fa fa-gear"></i>
                                            </button>
                                            <div class="dropdown-menu dropdown-menu-left">
                                                <a href="" class="dropdown-item" >Editar</a>
                                                <a href="" class="dropdown-item" >Eliminar</a>
                                            </div>
                                        </div>
                                    </div>
                                </td>
                        <td><?= $item['availability'] ?></td>
                          <td><?= $item['title'] ?></td>
                          <td><?= $item['stock'] ?></td>
                          <td class="text-primary">$<?= $item['sale'] ?></td>
                          <td class="text-primary">$<?= $item['rent'] ?></td>
                          
                          
                        </tr>
                      <?php } ?>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
           
          </div>
        </div>
      </div>