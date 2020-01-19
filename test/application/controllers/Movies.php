<?php

defined('BASEPATH') OR exit('No direct script access allowed');

class Movies extends CI_Controller {

    public function __construct() {
        parent::__construct();
        $this->url_api ='http://127.0.0.1:5000';
    }


    public function index() {

       $data['movies'] = array();

            $func_controller = 'movie/list';
            $result          = json_decode(file_get_contents($this->url_api . "/" . $func_controller, false), true);
            //print_r($result);
            if (!$result) {
                return print(json_encode(array(
                    'status' => "Error al consumir el service"
                )));
            }
            if ($result['status'] == 'success') {
                $data['movies'] = $result['data'];
            }

            $this->load->view('header.php');
            $this->load->view('list_movies.php', $data);
            $this->load->view('footer.php');

    }

    public function read_movie($id) {
        $data['id']    = $id;
        $data['movie'] = array();

        $context    = $this->mutils->create_context_get(array(
          'id_movie' => $id
        ));

         $func_controller    = 'movie/';
         $result             = json_decode(file_get_contents($this->url_api . "/" . $func_controller.$id, false, $context), true);

          if (!$result) {
              return print(json_encode(array(
                  'status' => "Error al consumir el service"
              )));
          }

          if ($result['status'] == 'success') {
              $data['movies'] = $result['data'];
          }

          $this->load->view('header.php');
          $this->load->view('read_movie.php', $data);
          $this->load->view('footer.php');

    }
}
