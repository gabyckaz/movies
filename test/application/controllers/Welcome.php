<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Welcome extends CI_Controller {

	public function __construct() {
			parent::__construct();
			$this->url_api ='http://127.0.0.1:5000/';
	}
	/**
	 * Index Page for this controller.
	 *
	 * Maps to the following URL
	 * 		http://example.com/index.php/welcome
	 *	- or -
	 * 		http://example.com/index.php/welcome/index
	 *	- or -
	 * Since this controller is set as the default controller in
	 * config/routes.php, it's displayed at http://example.com/
	 *
	 * So any other public methods not prefixed with an underscore will
	 * map to /index.php/welcome/<method_name>
	 * @see https://codeigniter.com/user_guide/general/urls.html
	 */
	 public function index() {
			$data['movies'] = array();
					 $result  = json_decode(file_get_contents($this->url_api, false), true);
					 if (!$result) {
							 return print(json_encode(array(
									 'status' => "Error al consumir el service"
							 )));
					 }
					 if ($result['status'] == 'success') {
							 $data['movies'] = $result['data'];
					 }
					 $this->load->view('header.php');
					 $this->load->view('welcome.php', $data);
					 $this->load->view('footer.php');

	 }
}
