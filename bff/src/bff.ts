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
      res.status(201).send({ success: 'Ranking added' });
    })
    .catch((err) => {
      if (err.response.status == 409) {
        res.status(409).send(err.response.data);
      } else {
        res.status(500).send({ error: err });
      }
    });
});

app.get('/products', async (req: Request, res: Response) => {
  axios
    .get(`${process.env.STORE_API}/v2/products`)
    .then((response) => {
      res.status(200).send(response.data);
    })
    .catch((err) => {
      res.status(500).send({ error: 'Cannot retrieve all the products, check products API logs for details' });
    });
});

app.get('/product', async (req: Request, res: Response) => {
  const productid = req.query.product_id;
  if (!productid) {
    res.status(400).send({ error: 'Please provide an ID' });
  } else {
    axios
      .get(`${process.env.STORE_API}/v2/products/${productid}`)
      .then((response) => {
        res.status(200).send(response.data);
      })
      .catch((err) => {
        if (err.response.status == 400) {
          res.status(400).send(err);
        } else if (err.response.status == 404) {
          res.status(404).send({ error: 'Product not found' });
        } else {
          res.status(500).send({ error: 'Cannot retrieve this product, check products API logs for details' });
        }
      });
  }
});

app.get('/coins', async (req: Request, res: Response) => {
  if (!req.headers.authorization) {
    res.send({ error: 'Token not found' });
  } else {
    const [, userToken]: any = req.headers.authorization?.split(" ");
    axios.get(`${process.env.SESSION_API}/coins`, {
      headers: {
        Authorization: 'Basic ' + userToken,
      },
    }).then((response) => {
      res.status(200).send(response.data.toString())
    }).catch((err) => {
      if(err.response.status == 400) {
        res.status(400).send({error: "Invalid token"});
      } else if(err.response.status == 404) {
        res.status(404).send({error: "User not found"});
      } else {
        res.status(500).send({error: "Internal error"})
      }
    })
  }
})

app.put('/coins', async (req: Request, res: Response) => {
  if (!req.headers.authorization) {
    res.send({ error: 'Token not found' });
  } else {
    const coins = req.body.coins;
    const [, userToken]: any = req.headers.authorization?.split(" ");
    axios.put(`${process.env.SESSION_API}/coins`, {
      coins: coins
    }, {
      headers: {
        Authorization: 'Basic ' + userToken,
      },
    }).then((response) => {
      res.status(200).send(response.data.toString())
    }).catch((err) => {
      if(err.response.status == 400) {
        res.status(400).send({error: "Invalid token"});
      } else if(err.response.status == 404) {
        res.status(404).send({error: "User not found"});
      } else {
        res.status(500).send({error: "Internal error"})
      }
    })
  }
})

app.post('/purchase/:product_id', async (req: Request, res: Response) => {
  const productid = req.params.product_id;

  if (!req.headers.authorization) {
    res.status(400).send({ error: 'Token not found' });
  } else if (!productid) {
    res.status(400).send({ error: 'Please provide a product ID' });
  } else {
    const [, onlyjwt]: any = req.headers.authorization?.split(' ');
    const secret = process.env.SECRET;
    try {
      jwt.verify(onlyjwt, secret as string);

      axios
        .get(`${process.env.CURRENT_API}/products/${productid}`)
        .then((response) => {
          axios
            .post(`${process.env.PAYMENT_API}/authorize`, null, {
              headers: {
                Authorization: 'Basic ' + onlyjwt,
              },
            })
            .then(() => {
              res.status(200).send(response.data);
            });
        })
        .catch((err) => {
          if (err.response.status == 404) {
            res.status(404).send({ error: 'Product not found' });
          } else {
            res.status(500).send({ error: 'Internal error' });
          }
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
        res.status(401).send({ error: 'Email already exists' });
      } else {
        res.status(500).send(err);
      }
    });
});

app.post('/login', async (req: Request, res: Response) => {
  const token = req.headers.authorization;

  if (!token) {
    res.status(401).send({ error: 'No Token Provided' });
  } else {
    axios
      .post(`${process.env.SESSION_API}/login`, null, {
        headers: {
          Authorization: `${token}`,
        },
      })
      .then((response) => {
        res.status(200).send(response.data);
      })
      .catch((err) => {
        if (err.response.status == 401) {
          res.status(401).send({ error: 'Invalid email/password or token' });
        } else {
          res.status(500).send({ error: 'Internal error' });
        }
      });
  }
});
export default app;
