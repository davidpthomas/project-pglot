import express from 'express'
import { AppContext } from './config'

var create_router = (ctx: any) => {
  var router = express.Router()
  router.get('/.well-known/did.json', handle_did_json_request(ctx))
  return router
}

var handle_did_json_request = (ctx: any) => (_req, res) => {
  if (!ctx.cfg.serviceDid.endsWith(ctx.cfg.hostname)) {
    return res.sendStatus(404)
  }
  res.json({
    '@context': ['https://www.w3.org/ns/did/v1'],
    id: ctx.cfg.serviceDid,
    service: [
      {
        id: '#bsky_fg',
        type: 'BskyFeedGenerator',
        serviceEndpoint: 'https://' + ctx.cfg.hostname,
      },
    ],
  })
}

export { create_router }

export default make_router