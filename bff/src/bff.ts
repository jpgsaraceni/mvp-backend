import app from './app';
import dotenv from 'dotenv';
import { Request, Response } from 'express';
import axios from 'axios';
import jwt from 'jsonwebtoken';
dotenv.config();

app.get('/ranking', async (req: Request, res: Response) => {
  axios
    .get(`${process.env.RANKING_API}/ranking`)
    .then((response) => {
      res.status(200).send(response.data);
    })
    .catch((err) => {
      res.status(500).send(err);
    });
});

app.post('/ranking', async (req: Request, res: Response) => {
  axios
    .post(`${process.env.RANKING_API}/addranking`, {
      name: req.body.name,
      score: req.body.score,
    })
    .then((response) => {
      res.status(201).send({success: 'Ranking added'});
    })
    .catch((err) => {
      res.status(500).send({ error: err });
    });
});

app.get('/products', async (req: Request, res: Response) => {
  axios
    .get(`${process.env.STORE_API}/products`)
    .then((response) => {
      res.status(200).send(response.data);
    })
    .catch((err) => {
      res.status(500).send({ error: 'Cannot retrieve all the products, check products API logs for details' });
    });
});

app.get('/product', async (req: Request, res: Response) => {
  const productid = req.body.product_id;
  if (!productid) {
    res.status(400).send({ error: 'Please provide an ID' });
  } else {
    axios
      .get(`${process.env.STORE_API}/product?product_id=${productid}`)
      .then((response) => {
        res.status(200).send(response.data);
      })
      .catch((err) => {
        if (err.response.status == 400) {
          res.status(400).send(err);
        } else {
          res.status(500).send({ error: 'Cannot retrieve this product, check products API logs for details' });
        }
      });
  }
});

app.post('/purchase/:product_id', async (req: Request, res: Response) => {
  const productid = req.params.product_id;
  const [, onlyjwt]: any = req.headers.authorization?.split(' ');
  const secret = process.env.SECRET;

  if (!productid) {
    res.status(400).send({ error: 'Please provide a product ID' });
  } else {
    try {
      jwt.verify(onlyjwt, secret as string);

      axios
        .get(`${process.env.CURRENT_API}/product?product_id=${productid}`)
        .then(() => {
          axios.post(`${process.env.PAYMENT_API}/authorize`, null, {
            headers: {
              Authorization: 'Bearer ' + onlyjwt,
            },
          });
        })
        .catch((err) => {
          res.status(400).send({ error: 'This Item does not exists' });
        });
    } catch (err) {
      res.status(401).send({ error: 'Invalid Token' });
    }
  }
});

app.post('/register', async (req: Request, res: Response) => {
  const email = req.body.email;
  const name = req.body.name;
  const password = req.body.password;

  axios
    .post(`${process.env.SESSION_API}/register`, {
      email: email,
      name: name,
      password: password,
    })
    .then(() => {
      res.status(201).send({ success: 'Account created' });
    })
    .catch((err) => {
      if (err.response.status == 400) {
        res.status(400).send({ error: 'Email already exists' });
      } else {
        res.status(500).send(err);
      }
    });
});

axios.post('/login', async (req: Request, res: Response) => {
    const email = req.body.email;
    const password = req.body.password;

    axios.post(`${process.env.SESSION_API}/login`, {
        email: email,
        password: password
    }).then((response) => {
        res.status(200).send(response.data);
    }).catch((err) => {
        if(err.response.status == 400) {
            res.status(400).send({error: 'Invalid email or password'});
        } else {
            res.status(500).send({error: 'Internal error'});
        }
    })
})
export default app;
