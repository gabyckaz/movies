<div class="main-panel">
      <!-- Navbar -->
      <nav class="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top " >
        <div class="container-fluid"style="background:#fff">
          <div class="navbar-wrapper" >
            <a class="navbar-brand" >Movie gallery</a>
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
      <!-- End Navbar -->
      <div class="content">
        <div class="container-fluid">
          <div class="row">
          <?php foreach ($movies as $item) { ?>
            <div class="col-md-4">
              <div class="card card-profile">
                <div class="card-avatar">
                  <a href="#pablo">
                    <img class="img" src="<?= $item['img'] ?>" />
                  </a>
                </div>
                <div class="card-body">
                  <h6 class="card-category text-gray">
                  <h4 class="card-title"><?= $item['title'] ?></h4>
                  <p class="card-description"><?= $item['desc'] ?></p>
                  <a href="<?= site_url('movies/read_movie/'. $item['id_movie']) ?>">Read More</a>
                </div>
              </div>
            </div>

            <?php
                        }
                        ?>
          </div>
        </div>
      </div>

    </div>
