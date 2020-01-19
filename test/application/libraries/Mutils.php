<?php

defined('BASEPATH') OR exit('No direct script access allowed');

class Mutils {
    public function create_context_get($params) {
        $context = stream_context_create(
                array('http' =>
                    array(
                        'method' => 'GET',
                        'header' => 'Content-type: application/x-www-form-urlencoded',
                        'content' => http_build_query(
                                $params
                        )
                    )
                )
        );
        return $context;
    }

}
